# Play-Annotation-Generator Annotation Review — RPO_200

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_200`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 1
- **Action Segments:** 98
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_PullBall` | Position_Unknown | Team_Unknown | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `19` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 34 | START | 34 | 63 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 34 | START | 34 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 34 | START | 34 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 34 | START | 34 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 34 | START | 34 | 84 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `19` | `18` | 40 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullBall` | Position_Unknown | `19` | `18` | 54 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `19` | `18` | 93 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_None` | 53 | 98 | 46 | inferred_complete_timeline |
| `Action_None` | 103 | 194 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 51 | 19 | inferred_complete_timeline |
| `Action_None` | 65 | 148 | 84 | inferred_complete_timeline |
| `Action_None` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 95 | 22 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 165 | 54 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 87 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 143 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 175 | 46 | inferred_complete_timeline |
| `Action_None` | 180 | 194 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 101 | 68 | inferred_complete_timeline |
| `Action_None` | 102 | 190 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 84 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 175 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 201 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 189 | 157 | inferred_complete_timeline |
| `Action_None` | 191 | 199 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 196 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 213 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 116 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 66 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 2–121 | 108 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 34–195 | 158 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 58–192 | 127 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 113–204 | 91 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 127–187 | 61 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 149–194 | 44 | 3 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 195–201 | 6 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 196–206 | 11 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 198–202 | 5 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 214–229 | 16 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 214–233 | 14 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 216–225 | 10 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 216–228 | 11 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 218–232 | 15 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 218–224 | 7 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 222–232 | 8 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 222–228 | 7 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 222–233 | 12 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 229–232 | 4 | 1 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 74 | 76 | 2 | 66.7% | 75 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `18` (Position_Unknown)
- ❌ Missing segment for action `Action_PullBall` on target `18` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `18` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [33-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-87] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-189] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-98] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-84] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-175] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-66] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-148] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-239] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>