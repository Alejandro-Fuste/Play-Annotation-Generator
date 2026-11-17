# Play-Annotation-Generator Annotation Review — Power_371

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_371`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `25` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `1` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 26 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 26 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 26 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `24` | `Group` | 0 | START | 35 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `25` | `Group` | 0 | START | 38 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `5` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `10` | 79 | START | 79 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `25` | `20` | 79 | START | 79 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `18` | `17` | 79 | START | 79 | 101 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 168 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 175 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 26–110
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 110 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 26–98
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 93 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `25`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 38–127
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 38 | 78 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 108 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 127 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 150 | 173 | 24 | inferred_complete_timeline |
| `Action_None` | 175 | 224 | 50 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–184
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 78 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 101 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 131 | 141 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 168 | 19 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `24`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 35–118
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 35 | 83 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 177 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 192 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `23`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 30–83
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 83 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 26–86
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `26`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 40–98
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 40 | 86 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 98 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 145 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 100 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 134 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 147 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 217 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–126
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 22 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 86 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 226 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `31` | Position_Unknown | Team_Unknown | 96–124 | 29 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 108–236 | 88 | 8 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 109–239 | 122 | 5 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 167–239 | 73 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 167–239 | 56 | 6 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 172–239 | 68 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 177–239 | 63 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 178–239 | 46 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 182–186 | 5 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 191–239 | 47 | 3 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 195–239 | 45 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 201–239 | 39 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 202–239 | 36 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 227–239 | 11 | 2 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `25` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 99 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [92-102] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-118] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-224] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-134] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-22] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-104] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-93] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-98] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-110] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-79] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-192] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [79-101] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [115-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [125-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [131-141] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-83] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-108] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-127] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-98] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-124] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-132] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-162] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-206] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-236] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-222] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-193] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-222] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-239] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-232] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-239] for track '38' has 1 frames without a visible bounding box.
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