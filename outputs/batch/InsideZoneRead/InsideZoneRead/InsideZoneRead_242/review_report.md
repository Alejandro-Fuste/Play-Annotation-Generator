# Play-Annotation-Generator Annotation Review — InsideZoneRead_242

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_242`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | QB | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_Keep` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `10` | `9` | 4 | START | 4 | 12 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 7 | START | 19 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 7 | START | 7 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 7 | START | 7 | 63 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 7 | START | 7 | 30 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `15` | `14` | 18 | END | 4 | 9 |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | QB | `15` | `14` | 22 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Keep` | QB | `15` | `14` | 35 | START | 45 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 48 | START | 85 | 93 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 75 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_Keep` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 58 | 141 | 84 | inferred_complete_timeline |
| `Action_None` | 147 | 179 | 33 | inferred_complete_timeline |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 55 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 16 | 13 | inferred_complete_timeline |
| `Action_None` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 47 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 75 | 21 | inferred_complete_timeline |
| `Action_None` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_None` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 160 | 12 | inferred_complete_timeline |
| `Action_None` | 163 | 167 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 12 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 75 | 57 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 30 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 63 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 13 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 7 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–8
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 8 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_None` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_None` | 29 | 183 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 20 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_None` | 15 | 174 | 160 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 61 | 58 | inferred_complete_timeline |
| `Action_None` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 114 | 38 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 84 | 81 | inferred_complete_timeline |
| `Action_None` | 94 | 208 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 72 | 69 | inferred_complete_timeline |
| `Action_None` | 82 | 195 | 114 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–55 | 39 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 27–42 | 16 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 28–210 | 181 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 45–50 | 6 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 67–210 | 135 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 70–73 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 75–210 | 136 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 79–210 | 107 | 6 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 85–210 | 123 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 94–100 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 100–151 | 35 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 116–210 | 94 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 121–123 | 3 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 126–210 | 83 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 130–210 | 80 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 132–188 | 48 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 203–205 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 7 != Inferred start 19
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_ReadDefender` on target `15` (QB)
- ⚠️ `Action_Keep` for actor_track_id `15` (QB): Annotated start 35 != Inferred start 45
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 484: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [4–18], lower_priority='Action_ZoneBlock' annotated_start=7, effective_Action_ZoneBlock_start=19.
- ⚠️ Action 'Action_None' range [4-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-34] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-63] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-16] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-29] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-30] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [4-12] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-7] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-8] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [4-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [45-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-93] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-183] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-13] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-77] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-123] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-188] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-118] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-161] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>