# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_200`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_200/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 202, Column 'Close On Quarterback': Unknown actor track ID '?' in entry '120,?'.
> - Row 202, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '133,?'.
> - Row 202, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '150,180;?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-122] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-121] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-136] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-106] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '18' has 9 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-17] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-68] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-148] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-155] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-180] for track '29' has 3 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.