# Play-Annotation-Generator Annotation Review — InsideZoneRead_311

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_311`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 0 | START | 0 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `18` | `17` | 15 | START | 15 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 18 | START | 18 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 18 | START | 35 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 18 | START | 18 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 18 | START | 18 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 18 | START | 18 | 27 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 34 | END | 15 | 34 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `15` | 39 | START | 39 | 43 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | RT | `17` | `16` | 44 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `16` | `15` | 46 | START | 46 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `16` | `15` | 70 | START | 70 | 84 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 34 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_Keep` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_Keep` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 227 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 74 | 60 | inferred_complete_timeline |
| `Action_None` | 76 | 143 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 39 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 80 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 111 | 25 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 30 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 25 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 89 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_None` | 112 | 227 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 84 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 111 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_None` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 39 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 39 | 25 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 137 | 90 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 91 | 77 | inferred_complete_timeline |
| `Action_None` | 95 | 239 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 41 | 27 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 74 | 82 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 42 | 28 | inferred_complete_timeline |
| `Action_None` | 44 | 93 | 50 | inferred_complete_timeline |
| `Action_None` | 101 | 156 | 56 | inferred_complete_timeline |
| `Action_None` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 139 | 125 | inferred_complete_timeline |
| `Action_None` | 141 | 151 | 11 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 148 | 134 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 212 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 137 | 123 | inferred_complete_timeline |
| `Action_None` | 142 | 158 | 17 | inferred_complete_timeline |
| `Action_None` | 161 | 213 | 53 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 113 | 99 | inferred_complete_timeline |
| `Action_None` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 184 | 57 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 17–237 | 195 | 12 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 88–239 | 152 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 96–239 | 144 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 98–99 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 104–239 | 129 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 148–239 | 84 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 220–239 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `17` (RT)
- ⚠️ Ambiguous match for action `Action_Keep` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 622: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '16' has invalid range: start=44, end=39. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [15–34], lower_priority='Action_ZoneBlock' annotated_start=18, effective_Action_ZoneBlock_start=35.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
- ⚠️ Action 'Action_None' range [15-39] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-137] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-41] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-82] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-184] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-143] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-239] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [39-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [46-56] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-227] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [15-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-30] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-131] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-189] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-169] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-223] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '26' has 2 frames without a visible bounding box.
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

</details>