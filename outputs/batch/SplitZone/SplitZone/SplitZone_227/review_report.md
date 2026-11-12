# Play-Annotation-Generator Annotation Review — SplitZone_227

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_227`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 38
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 14 | START | 15 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 14 | START | 15 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 14 | START | 15 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 14 | START | 15 | 248 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 14 | START | 15 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 14 | START | 15 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 14 | START | 15 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 14 | START | 15 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 14 | START | 15 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 14 | START | 15 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 14 | START | 15 | 216 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `20` | `20` | 200 | END | 217 | 217 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 217 | START | 217 | 217 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `14` | 220 | START | 220 | 309 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 220 | START | 220 | 243 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 220 | START | 220 | 309 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 220 | START | 220 | 241 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `21` | 220 | START | 220 | 309 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 225 | START | 225 | 248 |
| ✅ EXACT | `Action_SplitBlock` | WR1 | `0` | `0` | 225 | START | 225 | 309 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `16` | `16` | 244 | START | 244 | 309 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `13` | 249 | START | 249 | 382 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 309 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 15–313
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_SnapReceive` | 217 | 217 | 1 | inferred_complete_timeline |
| `Action_None` | 218 | 224 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 225 | 248 | 24 | inferred_complete_timeline |
| `Action_None` | 249 | 313 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–403
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 248 | 234 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 382 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 385 | 403 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 224 | 210 | inferred_complete_timeline |
| `Action_SplitBlock` | 225 | 309 | 85 | inferred_complete_timeline |
| `Action_None` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 345 | 129 | inferred_complete_timeline |
| `Action_None` | 350 | 419 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 219 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 309 | 90 | inferred_complete_timeline |
| `Action_None` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 219 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 309 | 90 | inferred_complete_timeline |
| `Action_None` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_BallSnap` | 217 | 217 | 1 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 241 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 291 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 301 | 309 | 9 | inferred_complete_timeline |
| `Action_None` | 310 | 327 | 18 | inferred_complete_timeline |
| `Action_None` | 330 | 419 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 219 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 309 | 90 | inferred_complete_timeline |
| `Action_None` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 219 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 243 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 244 | 309 | 66 | inferred_complete_timeline |
| `Action_None` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 266 | 50 | inferred_complete_timeline |
| `Action_None` | 276 | 419 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 419 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 385 | 169 | inferred_complete_timeline |
| `Action_None` | 394 | 419 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 318 | 102 | inferred_complete_timeline |
| `Action_None` | 321 | 411 | 91 | inferred_complete_timeline |
| `Action_None` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 15–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 350 | 134 | inferred_complete_timeline |
| `Action_None` | 354 | 403 | 50 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |
| `Action_None` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–361
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 216 | 202 | inferred_complete_timeline |
| `Action_None` | 217 | 361 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 30–32 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 308–325 | 17 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 359–419 | 61 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 374–387 | 14 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 375–381 | 7 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 419–419 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 23 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=217, end=200. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '20' has invalid range: start=217, end=200. Clamping end to start.
- ⚠️ Action 'Action_None' range [217-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-419] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-385] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-411] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-382] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [385-403] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-361] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-350] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-403] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [243-291] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-327] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-313] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-32] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-387] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-381] for track '26' has 1 frames without a visible bounding box.
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

</details>