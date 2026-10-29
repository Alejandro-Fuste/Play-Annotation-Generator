# Play-Annotation-Generator Annotation Review — DeepCross_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB3 | defense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 17 | START | 17 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 20 | START | 32 | 59 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 20 | START | 20 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 20 | START | 20 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 20 | START | 20 | 163 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB3 | `2` | `2` | 31 | START | 31 | 202 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 31 | END | 17 | 31 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 133 | START | 133 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_None` | 32 | 132 | 101 | inferred_complete_timeline |
| `Action_ThrowPass` | 133 | 141 | 9 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 202 | 186 | inferred_complete_timeline |
| `Action_None` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 219 | 234 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 239 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 121 | 105 | inferred_complete_timeline |
| `Action_None` | 123 | 167 | 45 | inferred_complete_timeline |
| `Action_None` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 239 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 239 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 163 | 144 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 169 | 177 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 59 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 101 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 166 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 106 | 87 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 163 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 70 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 167 | 151 | inferred_complete_timeline |
| `Action_None` | 169 | 177 | 9 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 232 | 48 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 46 | 30 | inferred_complete_timeline |
| `Action_None` | 49 | 91 | 43 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 167 | 50 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 239 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 46 | 30 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 59 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 31 | 202 | 172 | inferred_complete_timeline |
| `Action_None` | 203 | 225 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 225 | 209 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 197 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–239 | 232 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–113 | 114 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–101 | 90 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 64–67 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 75–239 | 154 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 85–130 | 23 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 111–157 | 47 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 118–239 | 122 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 120–151 | 32 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 194–239 | 46 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 201–235 | 20 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 201–239 | 34 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 209–239 | 15 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 84: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 84: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 84: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [17–31], lower_priority='Action_PassBlock' annotated_start=20, effective_Action_PassBlock_start=32.
- ⚠️ Action 'Action_None' range [17-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-197] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-239] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-161] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-167] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-232] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-202] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-113] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-59] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-101] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [169-239] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-46] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-239] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-91] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-70] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-163] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [169-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-183] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-217] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>