# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_353`
- **Input XML**: `outputs/batch/Power/Power/Power_353/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 705: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 706: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [20-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-308] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-352] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-248] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-343] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-286] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-359] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-293] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-332] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-284] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-313] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-332] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-289] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-341] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-355] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-286] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [250-261] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [267-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-314] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-305] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-249] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [250-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-293] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-303] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-335] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '21' starts at frame 250, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [250-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [256-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [262-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-301] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-311] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-336] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-325] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-350] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-354] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-351] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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