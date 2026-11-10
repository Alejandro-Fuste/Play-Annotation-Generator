# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_5`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-250] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [177-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [206-217] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [231-299] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-282] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-226] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-244] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-299] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-299] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-250] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-284] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-270] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-299] for track '26' has 1 frames without a visible bounding box.
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