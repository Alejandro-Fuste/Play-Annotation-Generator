# Play-Annotation-Generator Annotation Review — InsideZoneRead_362

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_362`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Keep` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 16 | START | 16 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 19 | START | 19 | 32 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 19 | START | 19 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 19 | START | 31 | 65 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 19 | START | 19 | 42 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `7` | `6` | 30 | END | 16 | 26 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `6` | 36 | START | 36 | 41 |
| ✅ EXACT | `Action_Keep` | QB | `7` | `6` | 42 | START | 42 | 51 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `12` | `11` | 48 | START | 48 | 88 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `7` | `6` | 61 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 88 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_None` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_Keep` | 42 | 51 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 78 | 63 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 47 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 48 | 88 | 41 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 155 | 61 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 30 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 65 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 75 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 72 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 88 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 218 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 42 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 27 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 163 | 148 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 182 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 62 | 47 | inferred_complete_timeline |
| `Action_None` | 66 | 88 | 23 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 79 | 64 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 57 | 42 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–74 | 57 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–82 | 42 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 3–19 | 10 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 19–23 | 5 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 26–239 | 203 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 27–85 | 22 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 32–144 | 106 | 5 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 44–239 | 151 | 10 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 50–215 | 151 | 6 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 78–108 | 24 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 86–236 | 123 | 6 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 94–150 | 46 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 96–239 | 118 | 4 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 107–183 | 70 | 3 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 109–141 | 33 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 113–239 | 123 | 3 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 149–237 | 89 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 196–239 | 33 | 4 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `7` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '6' has invalid range: start=61, end=51. Clamping end to start.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [16–30], lower_priority='Action_ZoneBlock' annotated_start=19, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [16-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-163] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-57] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [16-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [42-51] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-27] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-78] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-155] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-54] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-73] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-97] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-215] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-141] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-236] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-170] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-141] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-221] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-239] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>