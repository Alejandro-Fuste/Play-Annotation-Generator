# Play-Annotation-Generator Annotation Review — JetSweep_202

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `JetSweep_202`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 115
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `10` | 5 | START | 5 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 5 | START | 5 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `17` | `17` | 11 | START | 11 | 25 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 19 | END | 19 | 19 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `13` | 23 | START | 23 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `17` | 42 | START | 42 | 56 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 50 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_Toss` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_None` | 42 | 79 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 210 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 21 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 72 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 116 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 86 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 210 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–78 | 79 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–90 | 64 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 11–93 | 72 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 11–66 | 56 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 12–152 | 127 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 18–21 | 4 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 29–210 | 161 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 31–51 | 21 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 64–139 | 76 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 64–156 | 53 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 65–210 | 146 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 69–111 | 40 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 76–110 | 23 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 76–210 | 135 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 79–185 | 107 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 101–178 | 74 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 136–147 | 12 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 172–175 | 4 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallSnap' at frame 3 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 65 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-19] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-21] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [11-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [34-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [42-56] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-66] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-25] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-83] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-152] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-21] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-93] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-139] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-114] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-210] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-101] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-110] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-147] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>