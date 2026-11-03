# Play-Annotation-Generator Annotation Review — Post10to15_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_3`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunPostRoute` | WR3 | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 19 | START | 19 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 22 | START | 22 | 65 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `15` | `15` | 22 | START | 36 | 210 |
| ✅ EXACT | `Action_PassBlock` | RG | `18` | `18` | 22 | START | 22 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 22 | START | 22 | 127 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `21` | 22 | START | 22 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 35 | END | 19 | 35 |
| ✅ EXACT | `Action_RunPostRoute` | WR3 | `4` | `4` | 36 | START | 36 | 166 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 81 | START | 81 | 92 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 36 | 80 | 45 | inferred_complete_timeline |
| `Action_ThrowPass` | 81 | 92 | 12 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 99 | 81 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 111 | 158 | 48 | inferred_complete_timeline |
| `Action_None` | 164 | 168 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 78 | 60 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_RunPostRoute` | 36 | 166 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 65 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 118 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 61 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 210 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 50 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 127 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 65 | 47 | inferred_complete_timeline |
| `Action_None` | 69 | 172 | 104 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 192 | 174 | inferred_complete_timeline |
| `Action_None` | 198 | 203 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 46 | 28 | inferred_complete_timeline |
| `Action_None` | 54 | 107 | 54 | inferred_complete_timeline |
| `Action_None` | 109 | 210 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 155 | 137 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 114 | 96 | inferred_complete_timeline |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |
| `Action_None` | 153 | 181 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 188 | 170 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 103 | 85 | inferred_complete_timeline |
| `Action_None` | 111 | 127 | 17 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 139 | 121 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 156 | 138 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–71 | 38 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 70–80 | 4 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 81–210 | 116 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 92–210 | 109 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 101–210 | 60 | 6 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 147–210 | 54 | 4 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 166–185 | 20 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 186–210 | 9 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `15` (C): Annotated start 22 != Inferred start 36
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [19–35], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=36.
- ⚠️ Action 'Action_None' range [19-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-172] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [36-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-114] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-181] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-107] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-139] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-65] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-127] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-192] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-127] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-39] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-192] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-131] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-191] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>