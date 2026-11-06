# Play-Annotation-Generator Annotation Review — OutsideZoneRead_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_81`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 405 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 111 |
| ✅ EXACT | `Action_PressEdge` | RB | `5` | `5` | 112 | START | 112 | 149 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `12` | 115 | START | 115 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 117 | START | 117 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 117 | START | 117 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 117 | START | 117 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `20` | 117 | START | 117 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 117 | START | 117 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 136 | START | 136 | 172 |

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
- **Visible Frames:** 0–266
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 136 | 172 | 37 | inferred_complete_timeline |
| `Action_None` | 173 | 266 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PressEdge` | 112 | 149 | 38 | inferred_complete_timeline |
| `Action_None` | 150 | 419 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 405 | 406 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 153 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 134 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 170 | 35 | inferred_complete_timeline |
| `Action_None` | 171 | 284 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 132 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 151 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 173 | 275 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 170 | 54 | inferred_complete_timeline |
| `Action_None` | 171 | 283 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 137 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_None` | 171 | 381 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 346 | 347 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 385 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 386 | 387 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 419 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 366 | 367 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 419 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 31–319 | 269 | 9 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 135–363 | 227 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 150–155 | 6 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 171–255 | 74 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 182–184 | 3 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 227–233 | 7 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 260–264 | 5 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 274–358 | 29 | 6 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 274–419 | 146 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 275–296 | 11 | 3 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 283–354 | 32 | 5 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 293–419 | 127 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 313–402 | 29 | 7 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 347–411 | 53 | 7 | Undefined position; Undefined team |
| `37` | `64` | Position_Unknown | Team_Unknown | 384–405 | 19 | 3 | Undefined position; Undefined team |
| `38` | `69` | Position_Unknown | Team_Unknown | 393–419 | 27 | 1 | Undefined position; Undefined team |
| `39` | `70` | Position_Unknown | Team_Unknown | 393–400 | 8 | 1 | Undefined position; Undefined team |
| `40` | `71` | Position_Unknown | Team_Unknown | 394–415 | 19 | 2 | Undefined position; Undefined team |
| `41` | `73` | Position_Unknown | Team_Unknown | 399–400 | 2 | 1 | Undefined position; Undefined team |
| `42` | `74` | Position_Unknown | Team_Unknown | 401–419 | 17 | 2 | Undefined position; Undefined team |
| `43` | `75` | Position_Unknown | Team_Unknown | 406–410 | 5 | 1 | Undefined position; Undefined team |
| `44` | `77` | Position_Unknown | Team_Unknown | 415–418 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 91 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-405] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-346] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-385] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-386] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-419] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [115-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-366] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-151] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-275] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-283] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-129] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-217] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-225] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-309] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-355] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-363] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-176] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-255] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-294] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-341] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-358] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-282] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-296] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-320] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-332] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-366] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-371] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-402] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-351] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-393] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-398] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-411] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-402] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-419] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-400] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-396] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-415] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-410] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-419] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-410] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-418] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>