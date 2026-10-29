# Play-Annotation-Generator Annotation Review — DeepCross_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 11 | START | 11 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 14 | START | 27 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 14 | START | 14 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 14 | START | 14 | 155 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 14 | START | 14 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 14 | START | 14 | 126 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `11` | `11` | 26 | START | 26 | 190 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 26 | END | 11 | 26 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 109 | START | 109 | 120 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_None` | 27 | 108 | 82 | inferred_complete_timeline |
| `Action_ThrowPass` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 121 | 149 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 147 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 191 | 210 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 187 | 177 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 155 | 142 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 166 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 52 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 155 | 102 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 210 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 155 | 129 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 210 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 126 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 154 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 81 | 71 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 125 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 38 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 193 | 183 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 126 | 116 | inferred_complete_timeline |
| `Action_None` | 130 | 154 | 25 | inferred_complete_timeline |
| `Action_None` | 156 | 202 | 47 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 110 | 100 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 210 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 156 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 55–204 | 125 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 103–124 | 22 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 131–137 | 6 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 153–204 | 17 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 173–186 | 14 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 173–209 | 29 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 180–210 | 18 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 194–200 | 5 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 201–209 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [11–26], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [11-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-147] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-126] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-202] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-193] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-149] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-155] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [169-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-187] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-52] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-166] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [168-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-210] for track '18' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [157-166] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-189] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>