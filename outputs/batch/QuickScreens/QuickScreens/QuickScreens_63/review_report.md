# Play-Annotation-Generator Annotation Review — QuickScreens_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_63`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ScreenBlock` | WR3 | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR4 | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR4 | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `12` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 3 | START | 3 | 20 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 20 | END | 3 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_ScreenBlock` | WR3 | `9` | `9` | 21 | START | 21 | 65 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `13` | `13` | 28 | START | 28 | 39 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR4 | `12` | `12` | 29 | START | 29 | 42 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `12` | `12` | 49 | START | 49 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR4 | `12` | `12` | 64 | START | 64 | 85 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_None` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 28 | 39 | 12 | inferred_complete_timeline |
| `Action_None` | 40 | 157 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 144 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 83 | 81 | inferred_complete_timeline |
| `Action_None` | 85 | 180 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ScreenBlock` | 21 | 65 | 45 | inferred_complete_timeline |
| `Action_ScreenBlock` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_ScreenBlock` | 78 | 93 | 16 | inferred_complete_timeline |
| `Action_None` | 94 | 162 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 29 | 42 | 14 | inferred_complete_timeline |
| `Action_None` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_SecureCatch` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 132 | 180 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 30 | 28 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 63 | 8 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 41 | 39 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 69 | 22 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 145 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_None` | 21 | 40 | 20 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 69 | 17 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 129 | 28 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 51 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 180 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 45 | 43 | inferred_complete_timeline |
| `Action_None` | 47 | 67 | 21 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 108 | 180 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 31 | 141 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 12 | 10 | inferred_complete_timeline |
| `Action_None` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 32 | 40 | 9 | inferred_complete_timeline |
| `Action_None` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 75 | 23 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_None` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 63 | 61 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 152 | 150 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 74 | 72 | inferred_complete_timeline |
| `Action_None` | 76 | 110 | 35 | inferred_complete_timeline |
| `Action_None` | 112 | 159 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 175 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 121–124 | 4 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 177–180 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ScreenBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 2 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 2 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 4 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [3-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-175] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-97] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-152] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-63] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [21-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [73-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-69] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [64-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [94-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [132-180] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-74] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-159] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-51] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-63] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-180] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-25] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-141] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-41] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-69] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-12] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-40] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-75] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>