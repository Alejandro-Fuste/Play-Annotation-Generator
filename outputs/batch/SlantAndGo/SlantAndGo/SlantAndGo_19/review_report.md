# Play-Annotation-Generator Annotation Review — SlantAndGo_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SellRoute` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `19` | `19` | 19 | START | 19 | 21 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 33 | END | 19 | 33 |
| ✅ EXACT | `Action_SellRoute` | WR2 | `1` | `1` | 66 | START | 66 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR2 | `1` | `1` | 88 | START | 88 | 182 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 106 | START | 106 | 107 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 33 | 15 | inferred_complete_timeline |
| `Action_None` | 34 | 66 | 33 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_ThrowPass` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 47 | 29 | inferred_complete_timeline |
| `Action_None` | 62 | 69 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 65 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SellRoute` | 66 | 87 | 22 | inferred_complete_timeline |
| `Action_VerticalStem` | 88 | 182 | 95 | inferred_complete_timeline |
| `Action_VerticalStem` | 185 | 188 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 38 | 20 | inferred_complete_timeline |
| `Action_None` | 46 | 58 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 118 | 100 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 42 | 24 | inferred_complete_timeline |
| `Action_None` | 44 | 51 | 8 | inferred_complete_timeline |
| `Action_None` | 69 | 86 | 18 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 146 | 46 | inferred_complete_timeline |
| `Action_None` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_None` | 170 | 177 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 27 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_None` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 86 | 21 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 103 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–9
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 94 | 76 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 67 | 49 | inferred_complete_timeline |
| `Action_None` | 83 | 166 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 206 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 86 | 68 | inferred_complete_timeline |
| `Action_None` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 120 | 102 | inferred_complete_timeline |
| `Action_None` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 146 | 156 | 11 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 55 | 37 | inferred_complete_timeline |
| `Action_None` | 67 | 176 | 110 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 128 | 110 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 38–210 | 150 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 40–210 | 171 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 65–139 | 74 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 73–124 | 27 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 82–210 | 97 | 9 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 124–210 | 87 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 146–157 | 12 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 147–169 | 8 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 149–170 | 20 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 150–210 | 59 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 173–204 | 29 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 180–184 | 5 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 180–206 | 27 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 189–204 | 16 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 198–208 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 97 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [19-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [88-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [185-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-206] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-38] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-58] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-86] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-128] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-55] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-67] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-166] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [19-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [24-27] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-42] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-51] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-179] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-192] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-206] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-208] for track '40' has 3 frames without a visible bounding box.
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

</details>