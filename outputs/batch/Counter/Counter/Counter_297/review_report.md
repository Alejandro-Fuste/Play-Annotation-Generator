# Play-Annotation-Generator Annotation Review — Counter_297

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_297`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB3 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 103 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 104 | START | 104 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `11` | `10` | 107 | START | 107 | 124 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `18` | `17` | 107 | START | 120 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 107 | START | 107 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB3 | `9` | `8` | 107 | START | 107 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `21` | `20` | 107 | START | 107 | 114 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 117 | END | 104 | 117 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 128 | START | 128 | 149 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 150 | START | 150 | 216 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 149 | 22 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 216 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 242 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 230 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 208 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_None` | 135 | 169 | 35 | inferred_complete_timeline |
| `Action_None` | 176 | 217 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 124 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 208 | 70 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 147 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 186 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 203 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 208 | 208 | 1 | inferred_complete_timeline |
| `Action_None` | 209 | 229 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_BallSnap` | 104 | 112 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 155 | 26 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 218 | 31 | inferred_complete_timeline |
| `Action_None` | 224 | 233 | 10 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 114 | 8 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 137 | 208 | 72 | inferred_complete_timeline |
| `Action_None` | 209 | 235 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_None` | 135 | 151 | 17 | inferred_complete_timeline |
| `Action_None` | 171 | 226 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 222 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_None` | 147 | 153 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 132 | 8 | inferred_complete_timeline |
| `Action_None` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 269 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 154 | 51 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 203 | 36 | inferred_complete_timeline |
| `Action_None` | 207 | 220 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 246 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 144 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 208 | 62 | inferred_complete_timeline |
| `Action_None` | 209 | 221 | 13 | inferred_complete_timeline |
| `Action_None` | 227 | 240 | 14 | inferred_complete_timeline |
| `Action_None` | 251 | 261 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 269 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `30` | Position_Unknown | Team_Unknown | 157–162 | 6 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 161–269 | 109 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 162–179 | 18 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 169–246 | 78 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 186–222 | 24 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 190–214 | 25 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `18` (C): Annotated start 107 != Inferred start 120
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (CB3) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (LT) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [104–117], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=118.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 102 frames exceeds threshold 90 frames [start=107, end=208].
- ⚠️ Action 'Action_None' range [104-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-151] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-144] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-261] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-269] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [104-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-233] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-186] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-229] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-126] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-169] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-217] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-209] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-214] for track '27' has 1 frames without a visible bounding box.
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

</details>