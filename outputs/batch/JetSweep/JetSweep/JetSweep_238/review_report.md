# Play-Annotation-Generator Annotation Review — JetSweep_238

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_238`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 40 | START | 40 | 69 |
| ✅ EXACT | `Action_LeadBlock` | TE | `2` | `1` | 42 | START | 42 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 42 | START | 70 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 42 | START | 42 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `2` | 42 | START | 42 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 42 | START | 42 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 42 | START | 42 | 88 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 53 | START | 53 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 69 | END | 40 | 69 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 81 | START | 81 | 84 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `19` | `18` | 85 | START | 85 | 102 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 232 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 69 | 30 | inferred_complete_timeline |
| `Action_None` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_Toss` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 85 | 117 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 98 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_LeadBlock` | 42 | 83 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 88 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 121 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 69 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 107 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 92 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 128 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 92 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 142 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 81 | 42 | inferred_complete_timeline |
| `Action_None` | 85 | 113 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 86 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 72 | 33 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 112 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 66 | 27 | inferred_complete_timeline |
| `Action_None` | 88 | 125 | 38 | inferred_complete_timeline |
| `Action_None` | 127 | 211 | 85 | inferred_complete_timeline |
| `Action_None` | 218 | 234 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 119 | 80 | inferred_complete_timeline |
| `Action_None` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_None` | 138 | 190 | 53 | inferred_complete_timeline |
| `Action_None` | 196 | 238 | 43 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_None` | 121 | 127 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 74 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 95 | 56 | inferred_complete_timeline |
| `Action_None` | 97 | 156 | 60 | inferred_complete_timeline |
| `Action_None` | 158 | 186 | 29 | inferred_complete_timeline |
| `Action_None` | 194 | 220 | 27 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 291 | 58 | inferred_complete_timeline |
| `Action_None` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 120 | 81 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 52–102 | 51 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 53–67 | 15 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 73–98 | 13 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 75–329 | 239 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 79–95 | 16 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 82–86 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 103–150 | 48 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 115–329 | 206 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 133–182 | 50 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 140–329 | 153 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 140–247 | 73 | 5 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 141–329 | 178 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 152–199 | 48 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 162–329 | 168 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 163–329 | 167 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 168–213 | 22 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 172–277 | 105 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 186–329 | 100 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 192–238 | 39 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 220–315 | 79 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 229–314 | 75 | 3 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 233–236 | 4 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 250–326 | 77 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 250–329 | 80 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 256–329 | 74 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 262–329 | 44 | 2 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 312–329 | 18 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 320–322 | 3 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 322–329 | 8 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 101 frames exceeds threshold 90 frames [start=42, end=142].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [40–69], lower_priority='Action_ZoneBlock' annotated_start=42, effective_Action_ZoneBlock_start=70.
- ⚠️ Action 'Action_None' range [40-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [42-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-142] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-291] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-125] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-211] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-88] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-182] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-224] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-168] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-227] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-177] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-253] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-277] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-232] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-255] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-315] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-301] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-326] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-296] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>