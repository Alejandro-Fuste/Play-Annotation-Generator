# Play-Annotation-Generator Annotation Review — OutsideZoneRead_139

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_139`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | RB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_Keep` | RB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 5 | START | 5 | 9 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `14` | `13` | 8 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | RB | `12` | `11` | 20 | END | 5 | 18 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `12` | `11` | 24 | START | 24 | 32 |
| ⚠️ START CHANGED | `Action_Keep` | RB | `12` | `11` | 33 | START | 35 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 47 | START | 47 | 53 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 66 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 66 | 62 | inferred_complete_timeline |
| `Action_None` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 18 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_Keep` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 55 | 168 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 209 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 14 | 10 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 11 | 7 | inferred_complete_timeline |
| `Action_None` | 14 | 25 | 12 | inferred_complete_timeline |
| `Action_None` | 27 | 37 | 11 | inferred_complete_timeline |
| `Action_None` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_None` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_None` | 67 | 70 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 173 | 99 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 48 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 168 | 164 | inferred_complete_timeline |
| `Action_None` | 170 | 179 | 10 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 71 | 67 | inferred_complete_timeline |
| `Action_None` | 77 | 107 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 154 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 210 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 66 | 62 | inferred_complete_timeline |
| `Action_None` | 68 | 210 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 185 | 181 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `26` | Position_Unknown | Team_Unknown | 62–159 | 74 | 5 | Undefined position; Undefined team |
| `16` | `29` | Position_Unknown | Team_Unknown | 78–210 | 113 | 5 | Undefined position; Undefined team |
| `17` | `30` | Position_Unknown | Team_Unknown | 78–210 | 114 | 4 | Undefined position; Undefined team |
| `18` | `31` | Position_Unknown | Team_Unknown | 78–210 | 122 | 4 | Undefined position; Undefined team |
| `19` | `32` | Position_Unknown | Team_Unknown | 78–173 | 95 | 2 | Undefined position; Undefined team |
| `20` | `33` | Position_Unknown | Team_Unknown | 78–210 | 121 | 5 | Undefined position; Undefined team |
| `21` | `36` | Position_Unknown | Team_Unknown | 83–88 | 6 | 1 | Undefined position; Undefined team |
| `22` | `37` | Position_Unknown | Team_Unknown | 84–210 | 127 | 1 | Undefined position; Undefined team |
| `23` | `39` | Position_Unknown | Team_Unknown | 100–169 | 66 | 2 | Undefined position; Undefined team |
| `24` | `40` | Position_Unknown | Team_Unknown | 105–112 | 8 | 1 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 121–210 | 82 | 4 | Undefined position; Undefined team |
| `26` | `43` | Position_Unknown | Team_Unknown | 140–146 | 7 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 156–209 | 38 | 4 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 171–210 | 27 | 5 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 175–199 | 20 | 2 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 185–206 | 19 | 3 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 197–202 | 6 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 199–210 | 11 | 2 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 206–210 | 5 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `12` (2 segments found)
- ⚠️ `Action_Keep` for actor_track_id `12` (RB): Annotated start 33 != Inferred start 35
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [5–20], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=21.
- ⚠️ Action 'Action_None' range [5-168] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-71] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-48] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-185] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [5-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 21, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [21-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [24-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-168] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [5-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-37] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-48] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-173] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-173] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-206] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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