# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_4`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [0-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [58-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-133] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [0-60] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-66] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [50-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-231] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-130] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [180-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [187-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-11] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-16] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-55] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-30] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-127] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-161] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.