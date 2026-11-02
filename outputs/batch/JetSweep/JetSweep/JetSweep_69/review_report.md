# Play-Annotation-Generator Annotation Review — JetSweep_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR-F | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR-F | offense | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR-F | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_LeadBlock` | HB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR-F | `16` | `Group` | 0 | START | 32 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_JetMotion` | WR-F | `16` | `15` | 33 | START | 33 | 64 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `3` | 34 | START | 34 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `12` | 43 | START | 43 | 100 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LT | `19` | `18` | 43 | START | 47 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `1` | 43 | START | 43 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `3` | 43 | START | 50 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 43 | START | 43 | 100 |
| ✅ EXACT | `Action_SnapReceive` | RB | `8` | `7` | 49 | END | 34 | 49 |
| ✅ EXACT | `Action_Toss` | RB | `8` | `7` | 55 | START | 55 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR-F | `16` | `15` | 65 | START | 65 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `2` | `1` | 67 | START | 67 | 69 |
| ✅ EXACT | `Action_LeadBlock` | HB | `11` | `10` | 85 | START | 85 | 100 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_Toss` | 55 | 64 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 121 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_LeadBlock` | 85 | 100 | 16 | inferred_complete_timeline |
| `Action_None` | 101 | 239 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR-F — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 32–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 33 | 64 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 65 | 65 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 174 | 105 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE-Y — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 83 | 50 | inferred_complete_timeline |
| `Action_None` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 47–239
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 47 | 100 | 54 | inferred_complete_timeline |
| `Action_None` | 101 | 239 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 66 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 78 | 100 | 23 | inferred_complete_timeline |
| `Action_None` | 101 | 110 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 61 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 75 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 100 | 20 | inferred_complete_timeline |
| `Action_None` | 101 | 239 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 100 | 58 | inferred_complete_timeline |
| `Action_None` | 101 | 101 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 100 | 58 | inferred_complete_timeline |
| `Action_None` | 101 | 108 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 32 | 13 | inferred_complete_timeline |
| `Action_None` | 38 | 45 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 105 | 31 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_None` | 126 | 239 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LDE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 114 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RDE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 66 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>MLB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 61 | 28 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WLB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 72 | 39 | inferred_complete_timeline |
| `Action_None` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_None` | 88 | 230 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 81 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 207 | 174 | inferred_complete_timeline |
| `Action_None` | 209 | 239 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LCB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 36–67
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 36 | 67 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 46–48 | 3 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 72–239 | 160 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 82–232 | 145 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 116–239 | 124 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 122–239 | 118 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 128–239 | 102 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 197–239 | 43 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 198–235 | 16 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 218–229 | 6 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 226–228 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 233–235 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (LT): Annotated start 43 != Inferred start 47
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [34–49], lower_priority='Action_ZoneBlock' annotated_start=43, effective_Action_ZoneBlock_start=50.
- ⚠️ Action 'Action_None' range [34-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [67-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-75] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-61] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-207] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 101, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [101-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-45] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '15' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [65-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>