# Play-Annotation-Generator Annotation Review — Power_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_117`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_DownBlock` | RG | offense | `16` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 6 | START | 6 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 6 | START | 47 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 6 | START | 66 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 6 | START | 6 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 6 | START | 6 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 6 | START | 6 | 299 |
| ⚠️ START CHANGED | `Action_DownBlock` | RG | `16` | `13` | 191 | START | 206 | 244 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `19` | 191 | START | 193 | 200 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 192 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 299 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 47–299
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 203 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 299 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–238
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 238 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–298
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 292 | 287 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 298 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 66–298
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 66 | 128 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 152 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 172 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 244 | 39 | inferred_complete_timeline |
| `Action_None` | 254 | 268 | 15 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 298 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–286
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 286 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 86–299
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 106 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 284 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 85–299
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 212 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–272
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 243 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 272 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 299 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 299 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 299 | 294 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 6–299 | 294 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 6–292 | 269 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 34–299 | 154 | 8 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 179–299 | 102 | 7 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 183–299 | 80 | 7 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 193–299 | 91 | 6 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 215–299 | 79 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 231–299 | 68 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 233–238 | 6 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 248–292 | 32 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 275–299 | 19 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 289–291 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `16` (RG): Annotated start 191 != Inferred start 206
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 235: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ Row 236: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Track ID '11' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [6-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-286] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-272] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-292] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-298] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-299] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-16] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-279] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-257] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-220] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-268] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-212] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-106] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-169] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-284] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-198] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-268] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [193-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [204-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-283] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-266] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>