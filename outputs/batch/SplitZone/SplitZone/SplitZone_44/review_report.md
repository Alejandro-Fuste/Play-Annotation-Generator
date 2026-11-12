# Play-Annotation-Generator Annotation Review — SplitZone_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_44`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | WR | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 26 | START | 26 | 41 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `12` | 29 | START | 42 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 29 | START | 29 | 53 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `14` | `14` | 29 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `6` | 29 | START | 29 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 29 | START | 29 | 72 |
| ✅ EXACT | `Action_SplitBlock` | TE | `15` | `15` | 31 | START | 31 | 72 |
| ✅ EXACT | `Action_SnapReceive` | LG | `14` | `14` | 41 | END | 26 | 41 |
| ✅ EXACT | `Action_BlockSecondLevel` | WR | `7` | `7` | 51 | START | 51 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `4` | 68 | START | 68 | 264 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 72 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 264 | 197 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 102 | 77 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |
| `Action_None` | 249 | 264 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 51 | 72 | 22 | inferred_complete_timeline |
| `Action_None` | 73 | 165 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SplitBlock` | 31 | 72 | 42 | inferred_complete_timeline |
| `Action_None` | 73 | 117 | 45 | inferred_complete_timeline |
| `Action_None` | 120 | 269 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 72 | 44 | inferred_complete_timeline |
| `Action_None` | 73 | 89 | 17 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 41 | 16 | inferred_complete_timeline |
| `Action_None` | 42 | 165 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 41 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 72 | 31 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 53 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 72 | 18 | inferred_complete_timeline |
| `Action_None` | 73 | 83 | 11 | inferred_complete_timeline |
| `Action_None` | 96 | 269 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 72 | 44 | inferred_complete_timeline |
| `Action_None` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 161 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 109 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 119 | 94 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 120 | 95 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 247 | 222 | inferred_complete_timeline |
| `Action_None` | 250 | 262 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 48 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 228 | 203 | inferred_complete_timeline |
| `Action_None` | 230 | 238 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `21` | Position_Unknown | Team_Unknown | 106–269 | 164 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 109–269 | 161 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 110–269 | 98 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 113–269 | 157 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 114–269 | 156 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 125–177 | 52 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 129–269 | 141 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 139–268 | 118 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 140–144 | 5 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 175–269 | 95 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 175–269 | 94 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 193–243 | 8 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 213–264 | 52 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 29 != Inferred start 42
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (LG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [26–41], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=42.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=29, end=25. Clamping end to start.
- ⚠️ Action 'Action_None' range [26-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-102] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-264] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-228] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-161] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [73-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [73-83] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-187] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-268] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-264] for track '30' has 1 frames without a visible bounding box.
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

</details>