# Play-Annotation-Generator Annotation Review — JetSweep_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_51`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 45
- **Ball Tracks:** 2
- **Action Segments:** 104
- **Validation Warnings:** 134
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
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 47 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RG | `8` | `7` | 48 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `6` | `5` | 50 | START | 50 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 50 | START | 50 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `12` | 50 | START | 50 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 50 | START | 50 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 50 | START | 50 | 106 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `8` | `7` | 50 | START | N/A | N/A |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 60 | START | 60 | 76 |
| ✅ EXACT | `Action_SnapReceive` | RG | `8` | `7` | 63 | END | 48 | 63 |
| ✅ EXACT | `Action_Toss` | RG | `8` | `7` | 69 | START | 69 | 77 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `8` | `7` | 78 | START | 78 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 79 | START | 81 | 368 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 106 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 110 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_LeadBlock` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 53 | 93 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 74 | 27 | inferred_complete_timeline |
| `Action_None` | 76 | 104 | 29 | inferred_complete_timeline |
| `Action_None` | 106 | 125 | 20 | inferred_complete_timeline |
| `Action_None` | 164 | 389 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 85 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 106 | 15 | inferred_complete_timeline |
| `Action_None` | 107 | 389 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 106 | 57 | inferred_complete_timeline |
| `Action_None` | 107 | 120 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 106 | 57 | inferred_complete_timeline |
| `Action_None` | 107 | 139 | 33 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_Toss` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 78 | 106 | 29 | inferred_complete_timeline |
| `Action_None` | 107 | 142 | 36 | inferred_complete_timeline |
| `Action_None` | 147 | 268 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 106 | 57 | inferred_complete_timeline |
| `Action_None` | 107 | 133 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 69 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 122 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 59 | 12 | inferred_complete_timeline |
| `Action_None` | 95 | 102 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 76 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_None` | 95 | 389 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 78 | 31 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 347 | 250 | inferred_complete_timeline |
| `Action_None` | 349 | 389 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 72 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 111 | 64 | inferred_complete_timeline |
| `Action_None` | 171 | 238 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–387 | 381 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 50–139 | 79 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 60–380 | 308 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 100–131 | 32 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 107–114 | 8 | 1 | Undefined position; Undefined team |
| `21` | `33` | Position_Unknown | Team_Unknown | 113–389 | 277 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 115–118 | 4 | 1 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 120–389 | 257 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 123–148 | 26 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 126–389 | 240 | 2 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 129–389 | 261 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 137–389 | 253 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 146–269 | 113 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 152–233 | 82 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 158–389 | 232 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 178–233 | 56 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 205–347 | 143 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 277–389 | 96 | 4 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 296–313 | 6 | 2 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 332–344 | 11 | 2 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 352–374 | 23 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 352–357 | 4 | 2 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 352–357 | 4 | 2 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 353–377 | 25 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 371–383 | 13 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 372–375 | 4 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 378–385 | 7 | 2 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `36` | 119 | 120 | 2 | 100.0% | None |
| `28` | `44` | 135 | 135 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `8` (RG)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 104: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=50, end=47. Clamping end to start.
- ⚠️ Action 'Action_None' range [48-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-104] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-238] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [50-51] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [53-93] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-133] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-85] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-78] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-139] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-387] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-76] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-69] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-113] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [60-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-368] for track '18' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [378-380] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-389] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-233] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-233] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-347] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-321] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-368] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-344] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-374] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-377] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-383] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
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

</details>