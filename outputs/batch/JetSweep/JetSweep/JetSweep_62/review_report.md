# Play-Annotation-Generator Annotation Review — JetSweep_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_62`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | QB | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `20` | `19` |
| ✅ EXACT | `Action_Toss` | RB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `4` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `4` | `3` | 55 | START | 55 | 111 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 84 | START | 84 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | QB | `22` | `21` | 90 | START | 90 | 94 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `12` | `11` | 90 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 90 | START | 90 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 90 | START | 90 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `18` | 90 | START | 90 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 90 | START | 90 | 106 |
| ✅ EXACT | `Action_SnapReceive` | RB | `20` | `19` | 95 | END | 84 | 95 |
| ✅ EXACT | `Action_Toss` | RB | `20` | `19` | 101 | START | 101 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `4` | `3` | 112 | START | 112 | 197 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `19` | `18` | 120 | START | 120 | 137 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_LeadBlock` | 90 | 94 | 5 | inferred_complete_timeline |
| `Action_LeadBlock` | 97 | 137 | 41 | inferred_complete_timeline |
| `Action_None` | 138 | 167 | 30 | inferred_complete_timeline |
| `Action_None` | 171 | 189 | 19 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 84 | 95 | 12 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_Toss` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 112 | 271 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 260 | 177 | inferred_complete_timeline |
| `Action_None` | 271 | 280 | 10 | inferred_complete_timeline |
| `Action_None` | 283 | 297 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 273 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_JetMotion` | 55 | 111 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 197 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 210 | 263 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 278 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 289 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 137 | 48 | inferred_complete_timeline |
| `Action_None` | 138 | 275 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 134 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 137 | 1 | inferred_complete_timeline |
| `Action_None` | 138 | 192 | 55 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_BallSnap` | 84 | 94 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 89 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 137 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 119 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 120 | 137 | 18 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 149 | 66 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 275 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 236 | 153 | inferred_complete_timeline |
| `Action_None` | 243 | 256 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 133–275 | 136 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 156–179 | 11 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 177–297 | 121 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 254–266 | 4 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 267–271 | 5 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 269–296 | 19 | 3 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 273–282 | 10 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 276–291 | 16 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 276–294 | 19 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 280–284 | 5 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 283–290 | 8 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 292–296 | 5 | 1 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [84–94], lower_priority='Action_ZoneBlock' annotated_start=90, effective_Action_ZoneBlock_start=95.
- ⚠️ Action 'Action_None' range [84-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-263] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-289] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [84-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-275] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-271] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-128] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [90-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-189] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-275] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-297] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '38' has 1 frames without a visible bounding box.
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

</details>