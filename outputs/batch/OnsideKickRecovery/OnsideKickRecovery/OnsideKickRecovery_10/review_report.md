# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_10`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 2 | START | 2 | 58 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 59 | START | 59 | 112 |
| ✅ EXACT | `Action_AttemptRecovery` | Kicker | `15` | `15` | 113 | START | 113 | 118 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | `15` | `15` | 133 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 58 | 57 | inferred_complete_timeline |
| `Action_KickBall` | 59 | 112 | 54 | inferred_complete_timeline |
| `Action_AttemptRecovery` | 113 | 118 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 127 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 92 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 144 | 143 | inferred_complete_timeline |
| `Action_None` | 153 | 165 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 189 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 102 | 101 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 90 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 96 | 95 | inferred_complete_timeline |
| `Action_None` | 100 | 239 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 102 | 101 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 111 | 110 | inferred_complete_timeline |
| `Action_None` | 116 | 154 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 59 | 58 | inferred_complete_timeline |
| `Action_None` | 61 | 88 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 158 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 4 | 3 | inferred_complete_timeline |
| `Action_None` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 98 | 20 | inferred_complete_timeline |
| `Action_None` | 102 | 142 | 41 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 105 | 104 | inferred_complete_timeline |
| `Action_None` | 119 | 126 | 8 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 188 | 56 | inferred_complete_timeline |
| `Action_None` | 190 | 205 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 206 | 205 | inferred_complete_timeline |
| `Action_None` | 224 | 234 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 93 | 92 | inferred_complete_timeline |
| `Action_None` | 99 | 113 | 15 | inferred_complete_timeline |
| `Action_None` | 116 | 168 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 239 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 81 | 80 | inferred_complete_timeline |
| `Action_None` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 160 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 19–239 | 142 | 7 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 26–78 | 25 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 51–239 | 180 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 65–91 | 14 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 83–107 | 24 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 93–165 | 73 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 94–98 | 5 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 98–103 | 6 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 100–108 | 9 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 102–183 | 79 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 130–232 | 103 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 213–222 | 10 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureRecovery` on target `15` (Kicker)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Onside_Recovery_Front7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_SecureRecovery' for track '15' has invalid range: start=133, end=118. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-189] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-144] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-165] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-113] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-168] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_AttemptRecovery' range [113-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-98] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-142] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-191] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-122] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-107] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-165] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-232] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '33' has 1 frames without a visible bounding box.
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

</details>