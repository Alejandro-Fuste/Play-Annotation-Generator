# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_192`
- **Input XML**: `outputs/batch/Power/Power/Power_192/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 386: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [14-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-29] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-289] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-302] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [179-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-123] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-255] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-85] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-168] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-176] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-315] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-244] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-203] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-248] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-280] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-287] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-294] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-322] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-329] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-292] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.