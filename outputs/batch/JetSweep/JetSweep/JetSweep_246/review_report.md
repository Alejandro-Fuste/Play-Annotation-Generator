# Play-Annotation-Generator Annotation Review — JetSweep_246

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_246`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `14` | `13` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_JetMotion` | WR | `14` | `13` | 2 | START | 2 | 54 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 32 | START | 32 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `11` | `10` | 34 | START | 34 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 34 | START | 34 | 108 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 34 | START | 44 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `1` | 34 | START | 34 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 34 | START | 34 | 108 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 34 | START | 34 | 108 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 43 | END | 32 | 43 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 47 | START | 47 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `14` | `13` | 55 | START | 55 | 69 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_Toss` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 55 | 128 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 128 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 2 | 54 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 108 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_LeadBlock` | 34 | 85 | 52 | inferred_complete_timeline |
| `Action_LeadBlock` | 87 | 89 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 126 | 18 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 128 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 108 | 65 | inferred_complete_timeline |
| `Action_None` | 109 | 141 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 142 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 108 | 75 | inferred_complete_timeline |
| `Action_None` | 109 | 128 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 58 | 27 | inferred_complete_timeline |
| `Action_None` | 60 | 107 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 88 | 57 | inferred_complete_timeline |
| `Action_None` | 91 | 126 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 16 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 31 | 6 | inferred_complete_timeline |
| `Action_None` | 32 | 61 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 76 | 45 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 146 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 128 | 97 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 58 | 27 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 87 | 128 | 42 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 126 | 95 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 128 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 48 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | Position_Unknown | Team_Unknown | 75–128 | 54 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 81–128 | 48 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 111–142 | 26 | 4 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 113–128 | 16 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 129–138 | 10 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 129–134 | 6 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 129–234 | 106 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 129–140 | 12 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 129–144 | 16 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 129–133 | 5 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 129–149 | 21 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 129–134 | 6 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 129–239 | 109 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 134–239 | 102 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 136–239 | 104 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 136–138 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 137–239 | 98 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 34 != Inferred start 44
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [32–43], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=44.
- ⚠️ Action 'Action_ZoneBlock' range [34-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-48] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [34-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [87-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [135-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-16] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '36' has 1 frames without a visible bounding box.
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

</details>