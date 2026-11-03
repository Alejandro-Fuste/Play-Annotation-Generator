# Play-Annotation-Generator Annotation Review — PuntBlock_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_77`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 149
- **Validation Warnings:** 186
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 134
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Left_Guard | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `8` | `8` | 11 | START | 11 | 17 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 38 | END | 38 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `5` | `5` | 67 | START | 67 | 92 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Left_Guard | `14` | `14` | 75 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 69 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 33 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 58 | 18 | inferred_complete_timeline |
| `Action_None` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 72 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 34 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 63 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 66 | 28 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 92 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_PuntBall` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_PuntBall` | 131 | 140 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 34 | 24 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 170 | 124 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 58 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 116 | 106 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_None` | 22 | 60 | 39 | inferred_complete_timeline |
| `Action_None` | 62 | 101 | 40 | inferred_complete_timeline |
| `Action_None` | 107 | 158 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 16 | 6 | inferred_complete_timeline |
| `Action_None` | 23 | 90 | 68 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_None` | 101 | 116 | 16 | inferred_complete_timeline |
| `Action_None` | 118 | 171 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 38 | 28 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 46 | 66 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 94 | 27 | inferred_complete_timeline |
| `Action_None` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 130 | 14 | inferred_complete_timeline |
| `Action_None` | 146 | 154 | 9 | inferred_complete_timeline |
| `Action_None` | 156 | 224 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 139 | 129 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 27 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 101 | 73 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 137 | 19 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 157 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 102 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 107 | 97 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 25–127 | 101 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 27–239 | 205 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 44–239 | 179 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 101–174 | 71 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 117–239 | 100 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 125–196 | 20 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 125–179 | 50 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 131–157 | 19 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 138–183 | 35 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 142–163 | 22 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 143–239 | 91 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 144–225 | 75 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 147–236 | 84 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 151–163 | 13 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 153–239 | 87 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 154–230 | 32 | 3 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 172–214 | 22 | 4 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 176–221 | 44 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 186–214 | 20 | 3 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 186–214 | 18 | 5 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 195–224 | 30 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 234–237 | 4 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `5` (4 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `14` (Left_Guard)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 125 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BlockPunt' for track '14' has invalid range: start=75, end=69. Clamping end to start.
- ⚠️ Action 'Action_None' range [11-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-27] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-101] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-137] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-58] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [97-111] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [115-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [131-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-107] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [11-17] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [47-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-130] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-224] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-58] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-69] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-101] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-34] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-171] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-102] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-127] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-34] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-239] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-138] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-191] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-153] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-179] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-161] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-163] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-201] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-221] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-224] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '43' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>