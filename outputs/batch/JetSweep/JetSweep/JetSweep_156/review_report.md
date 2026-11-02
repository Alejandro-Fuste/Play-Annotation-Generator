# Play-Annotation-Generator Annotation Review — JetSweep_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_156`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `16` | `15` | 11 | START | 11 | 42 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 27 | START | 27 | 29 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 29 | START | 29 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 29 | START | 29 | 55 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 29 | START | 29 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 29 | START | 29 | 45 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `9` | `8` | 29 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 38 | END | 27 | 38 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 47 | START | 47 | 54 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `16` | `15` | 55 | START | 55 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `17` | `16` | 55 | START | 55 | 73 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 84 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–122
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 38 | 12 | inferred_complete_timeline |
| `Action_None` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_Toss` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 56 | 109 | 54 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 70 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 84 | 56 | inferred_complete_timeline |
| `Action_None` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 84 | 38 | inferred_complete_timeline |
| `Action_None` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 109 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 29 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 55 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 84 | 26 | inferred_complete_timeline |
| `Action_None` | 89 | 106 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 64 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 39 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 87 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_None` | 32 | 40 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 85 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 85 | 59 | inferred_complete_timeline |
| `Action_None` | 88 | 125 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 96 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 54 | 62 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 83 | 57 | inferred_complete_timeline |
| `Action_None` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 75 | 49 | inferred_complete_timeline |
| `Action_None` | 80 | 96 | 17 | inferred_complete_timeline |
| `Action_None` | 99 | 128 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 11–55 | 42 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 38–112 | 65 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 60–109 | 32 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 66–177 | 85 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 75–120 | 46 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 81–119 | 34 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 88–115 | 28 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 93–210 | 110 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 98–124 | 27 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 112–121 | 10 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 125–207 | 81 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 126–210 | 74 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 126–210 | 79 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 144–205 | 8 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 151–210 | 60 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 157–210 | 47 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 158–210 | 33 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 170–178 | 9 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 173–203 | 16 | 5 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 176–210 | 15 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 183–193 | 9 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 183–201 | 6 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 202–210 | 8 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (C)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [27–29], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=30.
- ⚠️ Action 'Action_ZoneBlock' range [29-84] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [47-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-85] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-87] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [27-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-106] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-83] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [11-42] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [45-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [51-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '15' starts at frame 55, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [55-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [55-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-112] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-88] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-177] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-120] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-103] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-159] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-207] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-141] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-199] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>