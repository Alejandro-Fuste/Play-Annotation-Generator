# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `FieldGoalBlock_105`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BlockKick' at frame 37 targets track ID '-', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 212: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 212: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [37-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-44] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-62] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-46] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-124] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-112] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-134] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-35] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-43] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-25] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-137] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-120] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-104] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-142] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-132] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-138] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-132] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-133] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-169] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '48' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.