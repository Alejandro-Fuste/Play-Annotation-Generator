# Play-Annotation-Generator Annotation Review — QuickScreens_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_25`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR3 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 24 | START | 24 | 38 |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | `0` | `0` | 38 | START | 38 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 38 | END | 24 | 38 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `14` | `14` | 56 | START | 56 | 65 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR3 | `2` | `2` | 59 | START | 59 | 80 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `2` | `2` | 85 | START | 85 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR3 | `2` | `2` | 93 | START | 93 | 133 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 56 | 65 | 10 | inferred_complete_timeline |
| `Action_None` | 66 | 180 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_None` | 47 | 79 | 33 | inferred_complete_timeline |
| `Action_None` | 81 | 180 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 129 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_ScreenBlock` | 38 | 88 | 51 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 59 | 80 | 22 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_SecureCatch` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 93 | 133 | 41 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 135 | 138 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 60 | 37 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_None` | 99 | 105 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 140 | 26 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 150 | 180 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 43 | 52 | 10 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 180 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 136 | 13 | inferred_complete_timeline |
| `Action_None` | 166 | 180 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 50 | 27 | inferred_complete_timeline |
| `Action_None` | 52 | 75 | 24 | inferred_complete_timeline |
| `Action_None` | 80 | 89 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 53 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 60 | 37 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_None` | 127 | 135 | 9 | inferred_complete_timeline |
| `Action_None` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 57 | 34 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 65 | 42 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 87 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 137 | 38 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 141 | 118 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 68 | 45 | inferred_complete_timeline |
| `Action_None` | 71 | 180 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 159 | 136 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 47–180 | 92 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 47–48 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 48–104 | 49 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 83–180 | 98 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 95–180 | 85 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 119–180 | 62 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 120–127 | 8 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 145–170 | 24 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 73 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ScreenBlock' range [38-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [93-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [135-138] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-60] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-105] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-65] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-87] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-159] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-141] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-155] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-170] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.

</details>