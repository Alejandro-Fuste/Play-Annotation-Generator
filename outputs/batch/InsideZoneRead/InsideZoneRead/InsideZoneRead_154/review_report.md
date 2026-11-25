# Play-Annotation-Generator Annotation Review — InsideZoneRead_154

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_154`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `18` | `17` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | RT | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 8 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 8 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 8 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 8 | 63 |
| ✅ EXACT | `Action_BallSnap` | RG | `18` | `17` | 64 | START | 64 | 66 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | `15` | `14` | 67 | START | 86 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 67 | START | 67 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `19` | 67 | START | 67 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `6` | 67 | START | 67 | 76 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `9` | `8` | 67 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | RT | `9` | `8` | 77 | END | 64 | 77 |
| ✅ EXACT | `Action_ReadDefender` | RT | `9` | `8` | 79 | START | 79 | 100 |
| ✅ EXACT | `Action_BallCarry` | RT | `9` | `8` | 101 | START | 101 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 117 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 8–220
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 149 | 86 | inferred_complete_timeline |
| `Action_None` | 155 | 173 | 19 | inferred_complete_timeline |
| `Action_None` | 175 | 190 | 16 | inferred_complete_timeline |
| `Action_None` | 194 | 220 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–237
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 173 | 110 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 220 | 39 | inferred_complete_timeline |
| `Action_None` | 223 | 237 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 117 | 32 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–108
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 108 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 117 | 33 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 117 | 51 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 79 | 100 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 239 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–188
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 188 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–208
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 161 | 98 | inferred_complete_timeline |
| `Action_None` | 164 | 208 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 8–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 148 | 85 | inferred_complete_timeline |
| `Action_None` | 150 | 156 | 7 | inferred_complete_timeline |
| `Action_None` | 158 | 239 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 8–237
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 145 | 82 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 182 | 21 | inferred_complete_timeline |
| `Action_None` | 185 | 234 | 50 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 8–154
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 142 | 79 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 8–147
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 147 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 8–230
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 221 | 158 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 107–239 | 119 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 118–132 | 6 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 157–239 | 83 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 168–237 | 69 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 204–226 | 22 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 216–239 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (LT): Annotated start 67 != Inferred start 86
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=67, end=63. Clamping end to start.
- ⚠️ Action 'Action_None' range [64-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-173] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-76] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-208] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-220] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-182] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-239] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_154'; source metadata written as null.

</details>