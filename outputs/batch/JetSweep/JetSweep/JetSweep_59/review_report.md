# Play-Annotation-Generator Annotation Review — JetSweep_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_59`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_SealBlock` | TE | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 45 | START | 45 | 58 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 52 | START | 52 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 52 | START | 52 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 52 | START | 52 | 70 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `8` | `8` | 52 | START | 67 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 52 | START | 52 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `15` | `15` | 53 | START | 53 | 76 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 58 | END | 45 | 58 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `10` | 64 | START | 64 | 82 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `12` | `12` | 78 | START | 78 | 122 |
| ✅ EXACT | `Action_BallCarry` | C | `8` | `8` | 83 | START | 83 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `5` | `5` | 83 | START | 83 | 103 |
| ✅ EXACT | `Action_SealBlock` | TE | `11` | `11` | 83 | START | 83 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_None` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_Toss` | 64 | 82 | 19 | inferred_complete_timeline |
| `Action_None` | 83 | 83 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 82 | 15 | inferred_complete_timeline |
| `Action_LeadBlock` | 83 | 103 | 21 | inferred_complete_timeline |
| `Action_LeadBlock` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_LeadBlock` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SealBlock` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 122 | 71 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 73 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 77 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 78 | 122 | 45 | inferred_complete_timeline |
| `Action_None` | 123 | 224 | 102 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 70 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 122 | 50 | inferred_complete_timeline |
| `Action_None` | 123 | 261 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 176 | 132 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 79 | 35 | inferred_complete_timeline |
| `Action_None` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 125 | 269 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 83 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 269 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 145 | 101 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 50–269 | 220 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 53–129 | 75 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 80–267 | 188 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 84–269 | 186 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 87–260 | 173 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 97–269 | 172 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 104–269 | 166 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 128–191 | 49 | 5 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 137–175 | 18 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 137–180 | 34 | 5 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 150–152 | 3 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 152–157 | 6 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 154–155 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 159–269 | 111 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 178–181 | 4 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 182–186 | 5 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 183–269 | 87 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `8` (C): Annotated start 52 != Inferred start 67
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [45–58], lower_priority='Action_ZoneBlock' annotated_start=52, effective_Action_ZoneBlock_start=59.
- ⚠️ Action 'Action_None' range [45-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [83-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [105-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [45-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [64-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 83, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [83-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [53-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [79-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '31' has 1 frames without a visible bounding box.
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

</details>