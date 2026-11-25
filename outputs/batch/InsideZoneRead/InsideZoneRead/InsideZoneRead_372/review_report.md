# Play-Annotation-Generator Annotation Review — InsideZoneRead_372

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_372`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | RB | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 19 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 17 | START | 58 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 20 | START | 20 | 23 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `10` | 20 | START | 20 | 105 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `15` | `14` | 20 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 20 | START | 20 | 24 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 20 | START | 20 | 105 |
| ✅ EXACT | `Action_SnapReceive` | RB | `13` | `12` | 30 | END | 17 | 30 |
| ✅ EXACT | `Action_ReadDefender` | RB | `13` | `12` | 36 | START | 36 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | RB | `13` | `12` | 44 | START | 44 | 49 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `13` | `12` | 70 | START | 72 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 38 | 22 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 43 | 50 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_None` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 36 | 43 | 8 | inferred_complete_timeline |
| `Action_Keep` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_Keep` | 54 | 62 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 178 | 162 | inferred_complete_timeline |
| `Action_None` | 197 | 239 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 24 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 105 | 1 | inferred_complete_timeline |
| `Action_None` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_None` | 123 | 239 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 105 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 105 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 165 | 60 | inferred_complete_timeline |
| `Action_None` | 169 | 215 | 47 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 38 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 156 | 140 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 38 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 100 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 36 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 84 | 68 | inferred_complete_timeline |
| `Action_None` | 88 | 124 | 37 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 225 | 95 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 85 | 69 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 63 | 47 | inferred_complete_timeline |
| `Action_None` | 65 | 195 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 97 | 81 | inferred_complete_timeline |
| `Action_None` | 100 | 169 | 70 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 14–17 | 4 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 58–145 | 78 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 58–97 | 37 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 64–239 | 176 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 66–239 | 140 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 75–78 | 4 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 93–117 | 20 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 123–232 | 110 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 132–239 | 108 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 133–137 | 5 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 134–140 | 7 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 134–239 | 104 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 141–239 | 96 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 152–165 | 14 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 166–239 | 74 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 170–235 | 48 | 5 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 175–238 | 63 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 183–187 | 5 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 186–239 | 24 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 188–195 | 8 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 188–239 | 52 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 203–209 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 17 != Inferred start 58
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `13` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `13` (RB): Annotated start 70 != Inferred start 72

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=20, end=19. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=58, end=30. Clamping end to start.
- ⚠️ Action 'Action_None' range [17-156] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-24] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-178] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-195] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-50] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [44-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [54-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [72-239] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-38] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 17, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [17-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-70] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-97] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-117] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-232] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-199] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-238] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-239] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_372'; source metadata written as null.

</details>