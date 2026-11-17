# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_189`
- **Input XML**: `outputs/batch/Power/Power/Power_189/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
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
> - Row 380: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 380: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 380: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-275] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-298] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-312] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-242] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-305] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-321] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-322] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-285] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-292] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-329] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-285] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-322] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-248] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-293] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-216] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [205-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-298] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-274] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-323] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-324] for track '28' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.