# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_52`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_None' range [118-383] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-263] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-367] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-416] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-352] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-390] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-213] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-360] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-419] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-238] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-271] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-366] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-279] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-214] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-419] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-380] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-293] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-335] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-419] for track '27' has 2 frames without a visible bounding box.
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