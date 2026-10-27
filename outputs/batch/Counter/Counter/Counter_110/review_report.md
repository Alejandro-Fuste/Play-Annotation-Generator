# Play-Annotation-Generator Annotation Review — Counter_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_110`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | defense | `15` | `14` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | LB1 | defense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 116 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `15` | `14` | 44 | START | 44 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `10` | 65 | START | 65 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT1 | `15` | `14` | 65 | START | 65 | 66 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `2` | `1` | 65 | START | 65 | 160 |
| ✅ EXACT | `Action_SnapReceive` | C | `13` | `12` | 75 | END | 44 | 75 |
| ✅ EXACT | `Action_Handoff` | LB1 | `3` | `2` | 102 | START | 102 | 121 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `9` | `8` | 122 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 160 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 65 | 160 | 96 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 90 | 47 | inferred_complete_timeline |
| `Action_None` | 93 | 101 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_DownBlock` | 65 | 115 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 181 | 15 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 75 | 32 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 199 | 115 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 101 | 58 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 87 | 44 | inferred_complete_timeline |
| `Action_None` | 89 | 107 | 19 | inferred_complete_timeline |
| `Action_None` | 112 | 130 | 19 | inferred_complete_timeline |
| `Action_None` | 132 | 144 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 170 | 16 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 135 | 92 | inferred_complete_timeline |
| `Action_None` | 140 | 199 | 60 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_None` | 80 | 155 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 44 | 64 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 86 | 160 | 75 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 94 | 51 | inferred_complete_timeline |
| `Action_None` | 97 | 136 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 102 | 121 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 87 | 44 | inferred_complete_timeline |
| `Action_None` | 89 | 136 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 62 | 19 | inferred_complete_timeline |
| `Action_None` | 66 | 71 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 183 | 140 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 93–210 | 115 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 107–152 | 45 | 2 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 122–199 | 78 | 1 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 137–210 | 71 | 2 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 151–168 | 18 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 152–210 | 59 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 158–207 | 50 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 171–196 | 25 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 175–210 | 36 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 183–210 | 26 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `9` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 221: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '8' has invalid range: start=122, end=116. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (LG) duration 96 frames exceeds threshold 90 frames [start=65, end=160].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (DT1) duration 96 frames exceeds threshold 90 frames [start=65, end=160].
- ⚠️ Action 'Action_None' range [44-183] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [65-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-130] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-144] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 161, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [161-164] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-181] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [44-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 76, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [76-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [65-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [78-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-152] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-199] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
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

</details>