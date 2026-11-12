# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_41`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [90–104], lower_priority='Action_ZoneBlock' annotated_start=93, effective_Action_ZoneBlock_start=105.
> - Action 'Action_None' range [90-266] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [109-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [131-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [155-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-245] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-269] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-269] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-196] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.