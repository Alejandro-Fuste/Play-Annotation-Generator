# Play-Annotation-Generator Annotation Review — Sack_136

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Sack_136`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Defense_Sack`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | Position_Unknown | Team_Unknown | `25` | `24` |
| ✅ EXACT | `Action_WrapQuarterback` | RB | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SackQuarterback` | RB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 11 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | Position_Unknown | `25` | `24` | 103 | START | 103 | 128 |
| ✅ EXACT | `Action_WrapQuarterback` | RB | `6` | `6` | 121 | START | 121 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_SackQuarterback` | RB | `6` | `6` | 127 | START | 127 | 138 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 11–93
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 93 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_SackQuarterback` | 127 | 138 | 12 | inferred_complete_timeline |
| `Action_SackQuarterback` | 141 | 150 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 152 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 154 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 197 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 19 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 59 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 134 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 171 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 210 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 164 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 177 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 134 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 174 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 184 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 202 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 207 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–209 | 209 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 56–120 | 65 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 98–210 | 71 | 8 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 98–155 | 56 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 99–209 | 81 | 7 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 128–166 | 11 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 128–145 | 15 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 131–196 | 56 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 138–183 | 27 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 153–192 | 33 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 162–176 | 12 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 162–203 | 35 | 4 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 163–208 | 46 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 176–197 | 7 | 3 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 190–201 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CloseOnQuarterback` and target `25` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SackQuarterback` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 109 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-197] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-202] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_WrapQuarterback' range [121-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [127-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [141-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-174] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-182] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-199] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [103-128] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [131-155] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-141] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-171] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-209] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-136] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-132] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-175] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-182] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-165] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-189] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-203] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-208] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-185] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-201] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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