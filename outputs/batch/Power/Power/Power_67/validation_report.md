# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_67`
- **Input XML**: `outputs/batch/Power/Power/Power_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 136: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [23-339] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-348] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-324] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-359] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-240] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-358] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-302] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-311] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-250] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-300] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-320] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-345] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-250] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-282] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-300] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [220-248] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-300] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-322] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-248] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-300] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-284] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-304] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-330] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-340] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-345] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-354] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [220-248] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [256-257] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-358] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-302] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-359] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-291] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-300] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-303] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-332] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-327] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-341] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-344] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [220-250] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-304] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-359] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [220-250] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [255-276] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [279-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-301] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-357] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-300] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-358] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-354] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-359] for track '29' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.