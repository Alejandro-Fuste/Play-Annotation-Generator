# Play-Annotation-Generator Annotation Review — Counter_127

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_127`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `21` | `20` | 37 | START | 37 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `13` | 39 | START | 39 | 85 |
| ✅ EXACT | `Action_DownBlock` | LT | `9` | `8` | 39 | START | 39 | 112 |
| ✅ EXACT | `Action_PullBlock` | RG | `22` | `21` | 39 | START | 39 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `17` | `16` | 39 | START | 39 | 46 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 51 | END | 37 | 51 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 69 | START | 69 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 87 | START | 87 | 167 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 112 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_None` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 69 | 86 | 18 | inferred_complete_timeline |
| `Action_None` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 167 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 170 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 155 | 119 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 186 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 66 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 39 | 112 | 74 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 39 | 85 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 112 | 26 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 44 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_None` | 58 | 164 | 107 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 189 | 203 | 15 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PullBlock` | 39 | 104 | 66 | inferred_complete_timeline |
| `Action_None` | 123 | 198 | 76 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 67 | 112 | 46 | inferred_complete_timeline |
| `Action_None` | 113 | 210 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 88 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 169 | 133 | inferred_complete_timeline |
| `Action_None` | 172 | 203 | 32 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 155 | 119 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 101 | 65 | inferred_complete_timeline |
| `Action_None` | 104 | 117 | 14 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 123 | 87 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 141 | 105 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 168 | 132 | inferred_complete_timeline |
| `Action_None` | 170 | 205 | 36 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 111 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 43–47 | 4 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 75–210 | 136 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 105–210 | 100 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 127–137 | 10 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 148–196 | 48 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 179–206 | 28 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 185–210 | 5 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 202–207 | 6 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [37-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-203] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-123] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-117] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-167] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-205] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [39-85] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-155] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [39-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [37-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [39-104] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-198] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
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

</details>