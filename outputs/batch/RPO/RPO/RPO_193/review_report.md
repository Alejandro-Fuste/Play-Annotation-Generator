# Play-Annotation-Generator Annotation Review — RPO_193

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_193`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 84
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `28` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_PullBall` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `7` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 55 | START | 55 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 55 | START | 55 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `18` | 55 | START | 55 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 55 | START | 55 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 55 | START | 55 | 113 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `16` | 74 | START | 74 | 85 |
| ⚠️ START CHANGED | `Action_PullBall` | QB | `16` | `16` | 90 | START | 91 | 96 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 123 | START | 123 | 132 |

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
- **Visible Frames:** 0–193
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 73 | 20 | inferred_complete_timeline |
| `Action_ReadDefender` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_PullBall` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 122 | 26 | inferred_complete_timeline |
| `Action_ThrowPass` | 123 | 132 | 10 | inferred_complete_timeline |
| `Action_None` | 133 | 193 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 158 | 105 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 87 | 34 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 143 | 90 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 120 | 67 | inferred_complete_timeline |
| `Action_None` | 123 | 194 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 130 | 76 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 113 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 131 | 77 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 74 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 132 | 30 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 54 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 132 | 78 | inferred_complete_timeline |
| `Action_None` | 133 | 178 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 148 | 95 | inferred_complete_timeline |
| `Action_None` | 160 | 177 | 18 | inferred_complete_timeline |
| `Action_None` | 179 | 209 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 135 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 131 | 78 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 136 | 83 | inferred_complete_timeline |
| `Action_None` | 138 | 170 | 33 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 118 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–105 | 106 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 78–95 | 13 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 100–210 | 62 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 147–203 | 50 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 160–182 | 20 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 172–210 | 33 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 175–210 | 33 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 180–183 | 4 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 189–210 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ `Action_PullBall` for actor_track_id `16` (QB): Annotated start 90 != Inferred start 91

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [54-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-136] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-170] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-87] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [74-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-74] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-131] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-184] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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