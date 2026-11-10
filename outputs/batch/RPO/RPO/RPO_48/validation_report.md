# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_48`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [21-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-104] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-77] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-286] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [22-76] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-285] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-77] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-179] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-281] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-275] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 21, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [21-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [24-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-249] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-272] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-275] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-320] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-311] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-304] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-307] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.