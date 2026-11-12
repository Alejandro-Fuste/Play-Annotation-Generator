# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_280`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_280/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 562: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_None' range [229-295] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-264] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-311] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-360] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-371] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-449] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [273-305] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [263-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [283-449] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-302] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [246-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [258-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-449] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-449] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-449] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-380] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-449] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-310] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-265] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-280] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-449] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-426] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-437] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '27' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.