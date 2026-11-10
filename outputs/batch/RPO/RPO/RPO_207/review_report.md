# Play-Annotation-Generator Annotation Review — RPO_207

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_207`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunInRoute` | actor_track_id `6` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 25 | START | 25 | 29 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 25 | START | 25 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 25 | START | 25 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 25 | START | 25 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 25 | START | 25 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `17` | `17` | 28 | START | 28 | 44 |
| ✅ EXACT | `Action_PullBall` | RB | `20` | `20` | 48 | START | 48 | 52 |
| ✅ EXACT | `Action_ThrowPass` | RB | `20` | `20` | 102 | START | 102 | 108 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 28 | 44 | 17 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 146 | 100 | inferred_complete_timeline |
| `Action_ReadDefender` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_ReadDefender` | 167 | 202 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 39 | 16 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_PullBall` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_None` | 53 | 101 | 49 | inferred_complete_timeline |
| `Action_ThrowPass` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 213 | 105 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 259 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 243 | 220 | inferred_complete_timeline |
| `Action_None` | 245 | 249 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 165 | 142 | inferred_complete_timeline |
| `Action_None` | 174 | 225 | 52 | inferred_complete_timeline |
| `Action_None` | 234 | 243 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 79 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 97 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 108 | 84 | inferred_complete_timeline |
| `Action_None` | 109 | 231 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 29 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 108 | 84 | inferred_complete_timeline |
| `Action_None` | 109 | 221 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 108 | 84 | inferred_complete_timeline |
| `Action_None` | 109 | 186 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 114 | 91 | inferred_complete_timeline |
| `Action_None` | 122 | 165 | 44 | inferred_complete_timeline |
| `Action_None` | 167 | 299 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 121 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 55 | 32 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 132 | 109 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 210 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 212 | 189 | inferred_complete_timeline |
| `Action_None` | 220 | 226 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–180 | 177 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–146 | 91 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 65–299 | 157 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 100–299 | 178 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 148–165 | 18 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 156–292 | 137 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 211–298 | 88 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 230–298 | 65 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 250–299 | 46 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 250–253 | 4 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 256–299 | 40 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 261–280 | 16 | 3 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 264–297 | 21 | 4 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 270–299 | 22 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 275–287 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 66 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [24-243] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-114] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-225] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-55] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-165] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-121] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [28-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [47-146] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [148-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [167-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-79] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-221] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-271] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-165] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-292] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-298] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-285] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-271] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>