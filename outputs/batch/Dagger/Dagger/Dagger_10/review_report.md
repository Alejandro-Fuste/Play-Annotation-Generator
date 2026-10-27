# Play-Annotation-Generator Annotation Review — Dagger_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_10`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_BreakInside` | WR1 | offense | `18` | `18` |
| ✅ EXACT | `Action_ClearToEdge` | WR3 | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `18` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 88 | START | 88 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 91 | START | 94 | 103 |
| ✅ EXACT | `Action_PassBlock` | RG | `15` | `15` | 91 | START | 91 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 91 | START | 91 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 91 | START | 91 | 212 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 91 | START | 91 | 263 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 93 | END | 88 | 93 |
| ✅ EXACT | `Action_BreakInside` | WR1 | `18` | `18` | 110 | START | 110 | 238 |
| ✅ EXACT | `Action_ClearToEdge` | WR3 | `4` | `4` | 110 | START | 110 | 192 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 184 | START | 184 | 192 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 94 | 183 | 90 | inferred_complete_timeline |
| `Action_ThrowPass` | 184 | 192 | 9 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 140 | 53 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_BreakInside` | 110 | 238 | 129 | inferred_complete_timeline |
| `Action_None` | 239 | 270 | 32 | inferred_complete_timeline |
| `Action_None` | 275 | 277 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 289 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ClearToEdge` | 110 | 192 | 83 | inferred_complete_timeline |
| `Action_None` | 193 | 235 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 263 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 212 | 122 | inferred_complete_timeline |
| `Action_PassBlock` | 214 | 217 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 103 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 201 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 221 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 188 | 98 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 272 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 246 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 193 | 106 | inferred_complete_timeline |
| `Action_None` | 219 | 227 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 212 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 214 | 127 | inferred_complete_timeline |
| `Action_None` | 216 | 226 | 11 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 211 | 124 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 232 | 145 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 299 | 212 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 35–86 | 23 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 124–127 | 4 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 177–240 | 57 | 4 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 192–215 | 24 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 208–226 | 19 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 225–299 | 73 | 3 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 240–245 | 6 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 268–299 | 31 | 2 | Undefined position; Undefined team |
| `35` | `59` | Position_Unknown | Team_Unknown | 281–290 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [88–93], lower_priority='Action_PassBlock' annotated_start=91, effective_Action_PassBlock_start=94.
- ⚠️ Action 'Action_None' range [88-289] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-193] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-246] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [110-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-272] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-299] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [203-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-221] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-232] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [110-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [214-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-263] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-65] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-221] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-240] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-215] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-288] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '35' has 1 frames without a visible bounding box.
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

</details>