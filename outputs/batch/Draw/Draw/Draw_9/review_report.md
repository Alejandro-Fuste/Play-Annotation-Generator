# Play-Annotation-Generator Annotation Review — Draw_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 44 | START | 44 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `12` | 47 | START | 60 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `16` | 47 | START | 47 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 47 | START | 47 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `22` | `21` | 47 | START | 47 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `8` | 47 | START | 47 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 59 | END | 44 | 59 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `14` | `13` | 62 | START | 62 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 90 | START | 90 | 98 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 62 | 89 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 87 | 44 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 106 | 63 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 171 | 128 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 121 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 134 | 10 | inferred_complete_timeline |
| `Action_None` | 135 | 210 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 76 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 134 | 33 | inferred_complete_timeline |
| `Action_None` | 135 | 193 | 59 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 109 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 71 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 85 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 134 | 44 | inferred_complete_timeline |
| `Action_None` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 87 | 44 | inferred_complete_timeline |
| `Action_None` | 96 | 151 | 56 | inferred_complete_timeline |
| `Action_None` | 154 | 196 | 43 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 43 | 10 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 99 | 56 | inferred_complete_timeline |
| `Action_None` | 101 | 200 | 100 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 149 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 134 | 91 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 206 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 210 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 109 | 66 | inferred_complete_timeline |
| `Action_None` | 111 | 180 | 70 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 208 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 82–210 | 129 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 92–102 | 8 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 108–111 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 135–174 | 14 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 150–159 | 10 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 159–210 | 52 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 180–210 | 30 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [44–59], lower_priority='Action_PassBlock' annotated_start=47, effective_Action_PassBlock_start=60.
- ⚠️ Action 'Action_None' range [44-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-149] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-200] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-76] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-210] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-151] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-193] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '31' has 1 frames without a visible bounding box.
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

</details>