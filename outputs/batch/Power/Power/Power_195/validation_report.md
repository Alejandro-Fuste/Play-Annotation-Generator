# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_195`
- **Input XML**: `outputs/batch/Power/Power/Power_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 392: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 392: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 392: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [18-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-262] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-294] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-234] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-168] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-280] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-215] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-139] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [143-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-220] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-272] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-249] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-278] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-287] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '27' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.