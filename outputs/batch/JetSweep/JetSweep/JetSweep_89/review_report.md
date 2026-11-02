# Play-Annotation-Generator Annotation Review — JetSweep_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_89`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ START CHANGED | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 2 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 4 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 76 | START | 76 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `16` | `15` | 80 | START | 80 | 95 |
| ⚠️ START CHANGED | `Action_LeadBlock` | Position_Unknown | `18` | `17` | 83 | START | 91 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 83 | START | 87 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 83 | START | 83 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 83 | START | 104 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 83 | START | 83 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 83 | START | 83 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 86 | END | 76 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `7` | `6` | 90 | START | 90 | 97 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `16` | `15` | 106 | START | 106 | 107 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `6` | `5` | 110 | START | 110 | 145 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 157 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–155
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_Toss` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_Toss` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 133 | 143 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 140 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–133
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 82 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 94 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 133 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 157 | 71 | inferred_complete_timeline |
| `Action_None` | 158 | 236 | 79 | inferred_complete_timeline |
| `Action_None` | 248 | 266 | 19 | inferred_complete_timeline |
| `Action_None` | 273 | 282 | 10 | inferred_complete_timeline |
| `Action_None` | 284 | 328 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–221
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 81 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 157 | 48 | inferred_complete_timeline |
| `Action_None` | 158 | 209 | 52 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 109 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 110 | 145 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 136 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 109 | 34 | inferred_complete_timeline |
| `Action_None` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_None` | 191 | 248 | 58 | inferred_complete_timeline |
| `Action_None` | 270 | 318 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 80 | 128 | 49 | inferred_complete_timeline |
| `Action_None` | 131 | 153 | 23 | inferred_complete_timeline |
| `Action_None` | 155 | 266 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 238 | 163 | inferred_complete_timeline |
| `Action_None` | 251 | 329 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 145 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 112 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 172 | 97 | inferred_complete_timeline |
| `Action_None` | 174 | 197 | 24 | inferred_complete_timeline |
| `Action_None` | 201 | 229 | 29 | inferred_complete_timeline |
| `Action_None` | 242 | 268 | 27 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 12–149 | 77 | 7 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 19–293 | 239 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 80–107 | 27 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 86–329 | 64 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 91–118 | 28 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 113–243 | 128 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 117–137 | 21 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 124–329 | 198 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 129–179 | 51 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 138–250 | 113 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 138–153 | 16 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 140–329 | 160 | 6 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 153–329 | 107 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 168–329 | 145 | 7 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 186–199 | 14 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 198–314 | 106 | 3 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 224–329 | 106 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 246–257 | 12 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 247–329 | 74 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 257–329 | 71 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 260–329 | 36 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 278–323 | 39 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 310–329 | 20 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `16` (2 segments found)
- ⚠️ `Action_LeadBlock` for actor_track_id `18` (Position_Unknown): Annotated start 83 != Inferred start 91
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [76–86], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=87.
- ⚠️ Action 'Action_None' range [76-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-197] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-229] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-109] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-128] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-266] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [110-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [90-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-282] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-133] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-209] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-149] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-140] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [80-95] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [91-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-189] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-250] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-153] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-329] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-271] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-314] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-315] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>