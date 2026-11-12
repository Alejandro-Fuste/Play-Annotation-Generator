# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_107`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [104–114], lower_priority='Action_ZoneBlock' annotated_start=107, effective_Action_ZoneBlock_start=115.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 107 frames exceeds threshold 90 frames [start=107, end=213].
> - Action 'Action_None' range [104-244] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-271] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-270] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [275-279] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [142-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-276] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-157] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-227] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-282] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-243] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-246] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-288] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-299] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.