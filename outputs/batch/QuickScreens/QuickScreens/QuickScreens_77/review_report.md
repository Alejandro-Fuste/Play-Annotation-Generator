# Play-Annotation-Generator Annotation Review — QuickScreens_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_77`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_ScreenBlock` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 3 | START | 3 | 18 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 18 | END | 3 | 18 |
| ✅ EXACT | `Action_ScreenBlock` | Position_Unknown | `8` | `8` | 24 | START | 24 | 108 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR2 | `1` | `1` | 27 | START | 27 | 42 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `10` | `10` | 32 | START | 32 | 38 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 49 | START | 49 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR2 | `1` | `1` | 75 | START | 75 | 110 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_None` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_None` | 39 | 178 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 103 | 101 | inferred_complete_timeline |
| `Action_None` | 106 | 137 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_None` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_SecureCatch` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_None` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 75 | 110 | 36 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 119 | 180 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 168 | 166 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 35 | 33 | inferred_complete_timeline |
| `Action_None` | 39 | 48 | 10 | inferred_complete_timeline |
| `Action_None` | 50 | 80 | 31 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 180 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 24 | 22 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_None` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_None` | 40 | 180 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 18 | 16 | inferred_complete_timeline |
| `Action_None` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 45 | 180 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 49 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 75 | 73 | inferred_complete_timeline |
| `Action_None` | 77 | 123 | 47 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 139 | 152 | 14 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 33 | 31 | inferred_complete_timeline |
| `Action_None` | 37 | 74 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 31 | 29 | inferred_complete_timeline |
| `Action_None` | 33 | 90 | 58 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_None` | 110 | 116 | 7 | inferred_complete_timeline |
| `Action_None` | 119 | 166 | 48 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_None` | 24 | 49 | 26 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 30 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 85 | 83 | inferred_complete_timeline |
| `Action_None` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 141 | 35 | inferred_complete_timeline |
| `Action_None` | 151 | 179 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 146 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 97 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 180 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 115 | 113 | inferred_complete_timeline |
| `Action_None` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_None` | 125 | 180 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–180 | 164 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 44–180 | 125 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 66–68 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 85–180 | 89 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 94–180 | 87 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 109–173 | 64 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 136–180 | 35 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 159–180 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 82: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [3-103] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [75-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [119-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-30] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-75] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-123] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-152] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-74] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [24-108] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-80] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-115] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-49] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-90] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-166] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-141] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-180] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-180] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-79] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-158] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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