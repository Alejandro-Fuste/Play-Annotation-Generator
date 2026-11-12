# Play-Annotation-Generator Annotation Review — SplitZone_315

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_315`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SplitBlock` | DT2 | defense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB3 | defense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | LB3 | defense | `17` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB3 | defense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 79 |
| ✅ EXACT | `Action_BallSnap` | QB | `18` | `18` | 71 | START | 71 | 76 |
| ✅ EXACT | `Action_SnapReceive` | C | `15` | `15` | 76 | END | 71 | 76 |
| ✅ EXACT | `Action_SplitBlock` | DT2 | `6` | `6` | 77 | START | 77 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 80 | START | 80 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 80 | START | 80 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `16` | 80 | START | 80 | 123 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `19` | `19` | 80 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 80 | START | 80 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LB3 | `17` | `17` | 97 | START | 97 | 104 |
| ✅ EXACT | `Action_Handoff` | LB3 | `17` | `17` | 105 | START | 105 | 111 |
| ✅ EXACT | `Action_BlockSecondLevel` | QB | `18` | `18` | 106 | START | 106 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB3 | `17` | `17` | 117 | START | 117 | 396 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 106 | 124 | 19 | inferred_complete_timeline |
| `Action_None` | 125 | 222 | 98 | inferred_complete_timeline |
| `Action_None` | 224 | 419 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 119 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 102–419
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 102 | 219 | 118 | inferred_complete_timeline |
| `Action_None` | 221 | 419 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 419 | 349 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 261 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 123 | 44 | inferred_complete_timeline |
| `Action_None` | 124 | 419 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 32 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 123 | 44 | inferred_complete_timeline |
| `Action_None` | 124 | 185 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 123 | 44 | inferred_complete_timeline |
| `Action_None` | 124 | 396 | 273 | inferred_complete_timeline |
| `Action_None` | 399 | 409 | 11 | inferred_complete_timeline |
| `Action_None` | 417 | 418 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 123 | 44 | inferred_complete_timeline |
| `Action_None` | 124 | 419 | 296 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 128 | 58 | inferred_complete_timeline |
| `Action_None` | 130 | 160 | 31 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 126–146
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 124 | 54 | inferred_complete_timeline |
| `Action_None` | 131 | 338 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SplitBlock` | 77 | 136 | 60 | inferred_complete_timeline |
| `Action_None` | 137 | 191 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 103 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 91 | 21 | inferred_complete_timeline |
| `Action_None` | 93 | 269 | 177 | inferred_complete_timeline |
| `Action_None` | 273 | 300 | 28 | inferred_complete_timeline |
| `Action_None` | 302 | 308 | 7 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_PressEdge` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_PressEdge` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 396 | 280 | inferred_complete_timeline |
| `Action_BallCarry` | 399 | 404 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 110 | 40 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 419 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 389 | 319 | inferred_complete_timeline |
| `Action_None` | 393 | 396 | 4 | inferred_complete_timeline |
| `Action_None` | 398 | 419 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 155 | 85 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 111 | 41 | inferred_complete_timeline |
| `Action_None` | 114 | 140 | 27 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 300 | 142 | inferred_complete_timeline |
| `Action_None` | 302 | 317 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–419 | 420 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 155–419 | 257 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 177–419 | 243 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 230–391 | 157 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 241–419 | 179 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 263–272 | 6 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (LG)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=80, end=32. Clamping end to start.
- ⚠️ Action 'Action_None' range [71-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-261] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-338] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-300] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-317] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-185] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-396] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-409] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-396] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [399-404] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-219] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-311] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-419] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-360] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-391] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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