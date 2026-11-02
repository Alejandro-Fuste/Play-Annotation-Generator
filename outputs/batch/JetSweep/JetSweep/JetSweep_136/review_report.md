# Play-Annotation-Generator Annotation Review — JetSweep_136

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_136`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `16` | 45 | START | 45 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 48 | START | 48 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `10` | `9` | 49 | START | 49 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 49 | START | 49 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `13` | 49 | START | 49 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 49 | START | 61 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 49 | START | 49 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 49 | START | 49 | 72 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 60 | END | 48 | 60 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 69 | START | 69 | 79 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `6` | `5` | 73 | START | 73 | 131 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `17` | `16` | 80 | START | 80 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–260
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_None` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_Toss` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 99 | 260 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_LeadBlock` | 49 | 109 | 61 | inferred_complete_timeline |
| `Action_LeadBlock` | 127 | 131 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 82 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 100 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 101 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 131 | 25 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 131 | 60 | inferred_complete_timeline |
| `Action_None` | 132 | 145 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 131 | 83 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 154 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 72 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 73 | 131 | 59 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 95 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 178 | 131 | inferred_complete_timeline |
| `Action_None` | 181 | 269 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 141 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 93 | 46 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 132 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 104 | 57 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_None` | 118 | 248 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 71 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 45–110 | 66 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 68–165 | 93 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 104–269 | 160 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 109–179 | 71 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 135–162 | 28 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 140–267 | 123 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 142–153 | 12 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 181–235 | 53 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 187–238 | 52 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 188–198 | 11 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 233–249 | 8 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 236–256 | 15 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 238–240 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 241–269 | 14 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 248–260 | 11 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 256–266 | 5 | 2 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [48–60], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=61.
- ⚠️ Action 'Action_None' range [48-71] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-248] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-178] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [49-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [69-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-260] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [48-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '14' starts at frame 61, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [61-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '33' has 1 frames without a visible bounding box.
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