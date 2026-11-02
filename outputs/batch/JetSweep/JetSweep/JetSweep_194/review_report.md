# Play-Annotation-Generator Annotation Review — JetSweep_194

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_194`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | WR | offense | `8` | `7` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 52 |
| ⚠️ START CHANGED | `Action_JetMotion` | WR | `8` | `7` | 28 | START | 33 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 52 | START | 52 | 60 |
| ✅ EXACT | `Action_LeadBlock` | TE | `9` | `8` | 53 | START | 53 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 53 | START | 63 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `1` | 53 | START | 53 | 56 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 53 | START | 53 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 53 | START | 53 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 61 | END | 52 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 69 | START | 69 | 70 |
| ✅ EXACT | `Action_BallCarry` | WR | `8` | `7` | 71 | START | 71 | 85 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 61 | 10 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_Toss` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 101 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_JetMotion` | 33 | 70 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 85 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_LeadBlock` | 53 | 100 | 48 | inferred_complete_timeline |
| `Action_None` | 101 | 154 | 54 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 206 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 100 | 48 | inferred_complete_timeline |
| `Action_None` | 101 | 115 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 58 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_BallSnap` | 52 | 60 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 100 | 23 | inferred_complete_timeline |
| `Action_None` | 101 | 106 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_None` | 125 | 134 | 10 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 90 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 127 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 67 | 101 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_None` | 82 | 112 | 31 | inferred_complete_timeline |
| `Action_None` | 116 | 183 | 68 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 35 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 99 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 70 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 78 | 27 | inferred_complete_timeline |
| `Action_None` | 80 | 96 | 17 | inferred_complete_timeline |
| `Action_None` | 98 | 212 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 9–96 | 51 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 57–222 | 156 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 75–142 | 37 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 86–151 | 48 | 2 | Undefined position; Undefined team |
| `17` | `25` | Position_Unknown | Team_Unknown | 94–96 | 3 | 1 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 95–239 | 145 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 97–215 | 116 | 3 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 101–161 | 61 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 125–130 | 6 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 141–146 | 6 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 145–239 | 89 | 2 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 149–239 | 91 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 171–176 | 4 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 210–226 | 4 | 2 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 223–239 | 15 | 2 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `8` (WR): Annotated start 28 != Inferred start 33
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [52–61], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=62.
- ⚠️ Action 'Action_None' range [52-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '1' starts at frame 53, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [53-56] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-46] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-212] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-58] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-101] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [33-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [71-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-206] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-35] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-127] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [52-60] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-142] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-104] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-155] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-215] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-231] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '30' has 1 frames without a visible bounding box.
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

</details>